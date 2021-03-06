#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os

from django.utils.translation import ugettext_lazy as _t

from desktop.lib.conf import Config, coerce_bool, coerce_csv


BASEDIR = os.path.dirname(os.path.abspath(__file__))


def dict_list_map(value):
  if isinstance(value, str):
    d = {}
    for k, v in json.loads(value).iteritems():
      d[k] = (v,)
    return d
  elif isinstance(value, dict):
    return value
  return None


XMLSEC_BINARY = Config(
  key="xmlsec_binary",
  default="/usr/local/bin/xmlsec1",
  type=str,
  help=_t("Xmlsec1 binary path. This program should be executable by the user running Hue."))

CREATE_USERS_ON_LOGIN = Config(
  key="create_users_on_login",
  default=True,
  type=coerce_bool,
  help=_t("Create users from IdP on login."))

ATTRIBUTE_MAP_DIR = Config(
  key="attribute_map_dir",
  default=os.path.abspath( os.path.join(BASEDIR, '..', '..', 'attribute-maps') ),
  type=str,
  private=True,
  help=_t("Attribute map directory contains files that map SAML attributes to pysaml2 attributes."))

ALLOW_UNSOLICITED = Config(
  key="allow_unsolicited",
  default=True,
  type=coerce_bool,
  private=True,
  help=_t("Allow responses that are initiated by the IdP."))

REQUIRED_ATTRIBUTES = Config(
  key="required_attributes",
  default=['uid'],
  type=coerce_csv,
  help=_t("Required attributes to ask for from IdP."))

OPTIONAL_ATTRIBUTES = Config(
  key="optional_attributes",
  default=[],
  type=coerce_csv,
  help=_t("Optional attributes to ask for from IdP."))

METADATA_FILE = Config(
  key="metadata_file",
  default=os.path.abspath( os.path.join(BASEDIR, '..', '..', 'examples', 'idp.xml') ),
  type=str,
  help=_t("IdP metadata in the form of a file. This is generally an XML file containing metadata that the Identity Provider generates."))

KEY_FILE = Config(
  key="key_file",
  default="",
  type=str,
  help=_t("key_file is the name of a PEM formatted file that contains the private key of the Hue service. This is presently used both to encrypt/sign assertions and as client key in a HTTPS session."))

CERT_FILE = Config(
  key="cert_file",
  default="",
  type=str,
  help=_t("This is the public part of the service private/public key pair. cert_file must be a PEM formatted certificate chain file."))

USER_ATTRIBUTE_MAPPING = Config(
  key="user_attribute_mapping",
  default={'uid': ('username', )},
  type=dict_list_map,
  help=_t("A mapping from attributes in the response from the IdP to django user attributes."))

AUTHN_REQUESTS_SIGNED = Config(
  key="authn_requests_signed",
  default=False,
  type=coerce_bool,
  help=_t("Have Hue initiated authn requests be signed and provide a certificate."))

LOGOUT_REQUESTS_SIGNED = Config(
  key="logout_requests_signed",
  default=False,
  type=coerce_bool,
  help=_t("Have Hue initiated logout requests be signed and provide a certificate."))