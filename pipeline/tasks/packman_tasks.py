# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tasks related to generation of packman tool"""

import subprocess

from pipeline.tasks import task_base
from pipeline.tasks.requirements import packman_requirements


class PackmanTaskBase(task_base.TaskBase):
    def run_packman(self, language, api_name, *additional_args):
        # Fix the api_name convention (ex. logging-v2) for packman.
        api_name = api_name.replace('-', '/')
        args = ['gen-api-package', '--api_name=' + api_name, '-l', language]
        args.extend(additional_args)
        subprocess.check_call(args)

    def validate(self):
        return [packman_requirements.PackmanRequirements]
