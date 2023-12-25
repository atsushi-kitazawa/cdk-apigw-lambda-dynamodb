import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_apigw_lambda_dynamodb.cdk_apigw_lambda_dynamodb_stack import CdkApigwLambdaDynamodbStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_apigw_lambda_dynamodb/cdk_apigw_lambda_dynamodb_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkApigwLambdaDynamodbStack(app, "cdk-apigw-lambda-dynamodb")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
