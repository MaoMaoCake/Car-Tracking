from flask import Blueprint, jsonify, request

from CarTrack import db
from CarTrack.models import Device