### Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html


{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:ap-northeast-1:391178969547:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:ap-northeast-1:391178969547:log-group:/aws/lambda/demolambda:*"
            ]
        }
    ]
}