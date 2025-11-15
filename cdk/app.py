#!/usr/bin/env python3
from aws_cdk import App, Environment
from personal_website_stack import PersonalWebsiteStack

app = App()

stack = PersonalWebsiteStack(
    app, 
    "PersonalWebsiteStack",
    env=Environment(
        account=app.node.try_get_context("account"),
        region=app.node.try_get_context("region") or "eu-west-1"  # Changed to eu-west-1
    ),
    description="Personal website infrastructure provided by Sébastien Grazzini"
)

app.synth()
