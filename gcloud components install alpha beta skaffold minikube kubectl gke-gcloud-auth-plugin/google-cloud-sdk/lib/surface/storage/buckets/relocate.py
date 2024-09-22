# -*- coding: utf-8 -*- #
# Copyright 2024 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Implementation of buckets relocate command."""

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.storage import flags


# TODO: b/361729720 - Make bucket-relocate command group universe compatible.
@base.Hidden
@base.DefaultUniverseOnly
@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Relocate(base.Command):
  """Relocates buckets, between different locations."""

  detailed_help = {
      'DESCRIPTION': """
      Relocates a bucket between different locations.
      """,

      'EXAMPLES': """
      To move a bucket (``gs://my-bucket'') to the ``us-central1'' location, use
      the following command:

          $ gcloud storage buckets relocate gs://my-bucket
              --location=us-central1

      To move a bucket to a custom Dual-region, use the following command:

          $ gcloud storage buckets relocate gs://my-bucket
              --placement=us-central1,us-east1

      To validate the operation without actually moving the bucket, use the
      following command:

          $ gcloud storage buckets relocate gs://my-bucket
              --location=us-central1 --dry-run

      To schedule a write lock for the move, use the following command:

          $ gcloud storage buckets relocate gs://my-bucket
              --location=us-central1 --finalize
      """,
  }

  @classmethod
  def Args(cls, parser):
    parser.SetSortArgs(False)
    parser.add_argument(
        'url', type=str, nargs=1, help='The URL of the bucket to relocate.'
    )
    parser.add_argument(
        '--location',
        type=str,
        help=(
            'The final location'
            ' (https://cloud.google.com/storage/docs/locations) where the'
            ' bucket will be relocated to. If no location is provided, Cloud'
            ' Storage will use the default location, which is us.'
        ),
    )
    flags.add_placement_flag(parser)
    operations = parser.add_mutually_exclusive_group()
    operations.add_argument(
        '--dry-run',
        action='store_true',
        help=(
            'Prints the operations that the relocate command would perform'
            ' without actually performing relocation. This is helpful to'
            ' identify any issues that need to be detected asynchronously.'
        ),
    )
    operations.add_argument(
        '--finalize',
        action='store_true',
        help=(
            'Schedules the write lock to occur. Once activated, no further'
            ' writes will be allowed to the associated bucket. This helps'
            ' minimize disruption to bucket usage. For certain types of'
            ' moves(between Multi Region and Custom Dual Regions), finalize is'
            ' not required.'
        ),
    )

  def Run(self, args):
    # TODO: b/361015951 - Implementation of relocate command
    raise NotImplementedError
