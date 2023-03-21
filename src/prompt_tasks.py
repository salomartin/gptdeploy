from src.constants import EXECUTOR_FILE_NAME, REQUIREMENTS_FILE_NAME, TEST_EXECUTOR_FILE_NAME, DOCKER_FILE_NAME, \
    DOCKER_FILE_TAG, CLIENT_FILE_TAG, CLIENT_FILE_NAME, STREAMLIT_FILE_TAG, STREAMLIT_FILE_NAME, EXECUTOR_FILE_TAG, \
    REQUIREMENTS_FILE_TAG, TEST_EXECUTOR_FILE_TAG


def general_guidelines():
    return (
        "The code you write is production ready. "
        "Every file starts with comments describing what the code is doing before the first import. "
        "Comments can only be written between tags. "
        "Then all imports are listed. "
        "It is important to import all modules that could be needed in the executor code. "
        "Always import: "
        "from typing import Dict, List, Optional, Tuple, Union "
        "from io import BytesIO "
        "from jina import Executor, DocumentArray, Document, requests "
        "Start from top-level and then fully implement all methods. "
        "\n"
    )


def _task(task, tag_name, file_name):
    return (
            task + f"The code will go into {file_name}. Wrap the code is wrapped into:\n"
                   f"**{file_name}**\n"
                   f"```{tag_name}\n"
                   f"...code...\n"
                   f"```\n\n"
    )


def executor_file_task(executor_name, executor_description, input_modality, input_doc_field,
                       output_modality, output_doc_field):
    return _task(
        f"Write the executor called '{executor_name}'. "
        f"It matches the following description: '{executor_description}'. "
        f"It gets a DocumentArray as input where each document has the input modality '{input_modality}' that is stored in document.{input_doc_field}. "
        f"It returns a DocumentArray as output where each document has the output modality '{output_modality}' that is stored in document.{output_doc_field}. "
        f"Have in mind that d.uri is never a path to a local file. It is always a url.",
        EXECUTOR_FILE_TAG,
        EXECUTOR_FILE_NAME
    )


def requirements_file_task():
    return _task(
        "Write the content of the requirements.txt file. "
        "Make sure to include pytest. "
        "All versions are fixed. ",
        REQUIREMENTS_FILE_TAG,
        REQUIREMENTS_FILE_NAME
    )


def test_executor_file_task(executor_name, test_in, test_out):
    return _task(
        "Write a small unit test for the executor. "
        "Start the test with an extensive comment about the test case. "
        + ((
                   "Test that the executor converts the input '" + test_in + "' to the output '" + test_out + "'. "
           ) if test_in and test_out else "")
        + "Use the following import to import the executor: "
          f"from executor import {executor_name} ",
        TEST_EXECUTOR_FILE_TAG,
        TEST_EXECUTOR_FILE_NAME
    )


def docker_file_task():
    return _task(
        "Write the Dockerfile that defines the environment with all necessary dependencies that the executor uses. "
        "The Dockerfile runs the test during the build process. "
        "It is important to make sure that all libs are installed that are required by the python packages. "
        "Usually libraries are installed with apt-get. "
        "Add the config.yml file to the Dockerfile. "
        "The base image of the Dockerfile is FROM jinaai/jina:3.14.1-py39-standard. "
        'The entrypoint is ENTRYPOINT ["jina", "executor", "--uses", "config.yml"] '
        "The Dockerfile runs the test during the build process. ",
        DOCKER_FILE_TAG,
        DOCKER_FILE_NAME
    )


def client_file_task():
    return _task(
        "Write the client file. ",
        CLIENT_FILE_TAG,
        CLIENT_FILE_NAME
    )


def streamlit_file_task():
    return _task(
        "Write the streamlit file allowing to make requests . ",
        STREAMLIT_FILE_TAG,
        STREAMLIT_FILE_NAME
    )