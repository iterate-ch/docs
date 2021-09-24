#!/usr/bin/env bash
#
# Copyright (c) 2002-2021 iterate GmbH. All rights reserved.
# https://cyberduck.io/
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

TARGET=s3:/github-cyberduck-docs
DIRECTORY=$1
[ ! $DIRECTORY ] && exit 1

echo "Updating $TARGET with $DIRECTORY"

echo "Deleting $TARGET"
duck -qy --username $AWS_ACCESS_KEY_ID --password $AWS_SECRET_ACCESS_KEY --delete "$TARGET/*" 
echo "Upload $DIRECTORY to $TARGET"
duck -qy --username $AWS_ACCESS_KEY_ID --password $AWS_SECRET_ACCESS_KEY --existing compare --upload "$TARGET" "$DIRECTORY/" --region $AWS_DEFAULT_REGION
echo "Purging $TARGET CDN configuration"
duck -qy --username $AWS_ACCESS_KEY_ID --password $AWS_SECRET_ACCESS_KEY --purge "$TARGET/"
