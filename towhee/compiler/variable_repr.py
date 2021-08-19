# Copyright 2021 Zilliz. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class VariableRepr:
    """
    The representation of a variable at compile-phase
    """

    def __init__(self, name: str, from_op: str):
        self.from_op = from_op
        self.to_op = []
        self.name = name
        self.type: type
        self.dtype: type


class VariableSet:
    """
    A set of VariableRepr
    """

    def __getattr__(self, name):
        raise NotImplementedError
        return self._var_dict[name]

    def from_dict(self, var_dict: [str, VariableRepr]):
        """
        Add variable from dict
        """
        raise NotImplementedError

    def add_var(self, key: str, var: VariableRepr):
        """
        Add a variable
        """
        raise NotImplementedError

