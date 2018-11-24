#!/bin/python
from ansible.module_utils.basic import *

def another_function():
  module = AnsibleModule(argument_spec={})
  response = {"hello": "world"}
  module.exit_json(changed=False, meta=response)

def custom_function():
  print("this is custom module")
  another_function()

def main():
  custom_function()

if __name__ == '__main__' :
  main()

