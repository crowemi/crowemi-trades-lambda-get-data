FROM public.ecr.aws/lambda/python:3.9

RUN yum -y update
RUN yum -y install git

# Copy function code
COPY get_data.py ${LAMBDA_TASK_ROOT}

# Install dependencies
RUN python -m pip install --upgrade pip
# TODO: add poetry install for consistenancy
RUN pip install git+https://github.com/crowemi/crowemi-trades.git@0.1.5
RUN pip install git+https://github.com/crowemi/crowemi-helps.git@0.1.5


CMD [ "get_data.handler" ]