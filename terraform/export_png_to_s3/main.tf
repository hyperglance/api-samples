provider "aws" {
  region = var.aws_region

  # Make it faster by skipping some things
  skip_get_ec2_platforms      = true
  skip_metadata_api_check     = true
  skip_region_validation      = true
  skip_credentials_validation = true
  skip_requesting_account_id  = true
}

data "aws_caller_identity" "current" {}

module "s3_deploy" {
  source = "../modules/aws-s3"

  bucket_name = "hyperglance-topology"
}

module "lambda_deploy" {
  source = "../modules/aws-lambda"

  lambda_function_name = "hyperglance_export_topology"
  lambda_source_file   = "hyperglance_export_topology.py"
  lambda_runtime       = "python3.8"

  iam_policy_statement = {
    s3_write = {
      effect    = "Allow",
      actions   = ["s3:PutObject", "kms:Decrypt"],
      resources = ["${module.s3_deploy.this_bucket_arn}/*", "arn:aws:kms:*:${data.aws_caller_identity.current.account_id}:key/*"]
    }
  }

  environment_variables = {
    API_KEY           = var.API_KEY,
    API_KEY_NAME      = var.API_KEY_NAME,
    BUCKET_NAME       = module.s3_deploy.this_bucket_name,
    EXPORT_DATASOURCE = var.EXPORT_DATASOURCE
    EXPORT_ACCOUNT    = var.EXPORT_ACCOUNT,
    EXPORT_ID         = var.EXPORT_ID,
    HYPERGLANCE_IP    = var.HYPERGLANCE_IP
  }

}

module "eventBridge_deploy" {
  source = "../modules/aws-eventbridge"

  // Uncomment the parameter below to change the schedule
  // event_schedule = "rate(1 day)"

  event_target_arn   = module.lambda_deploy.this_lambda_function_arn
  target_lambda_name = module.lambda_deploy.this_lambda_function_name
}