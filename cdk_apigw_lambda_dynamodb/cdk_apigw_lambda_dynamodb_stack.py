from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    aws_iam as iam
)
from constructs import Construct


class CdkApigwLambdaDynamodbStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # DynamoDB テーブルの作成
        table = dynamodb.Table(
            self, "MyTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )

        # Lambda 関数の作成
        lambda_function = lambda_.Function(
            self, "MyLambda",
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="index.handler",
            code=lambda_.InlineCode(
                "def handler(event, context):\n    return {'statusCode': 200, 'body': 'Hello from Lambda!'}"),
            environment={
                'TABLE_NAME': table.table_name
            }
        )

        # DynamoDB へのアクセス権を Lambda に付与
        table.grant_read_write_data(lambda_function)

        # API Gateway の作成
        api = apigateway.LambdaRestApi(
            self, "MyApi",
            handler=lambda_function,
            proxy=False
        )

        # API Gateway にリソースとメソッドを追加
        item = api.root.add_resource("item")
        item.add_method("GET")  # GET /item
