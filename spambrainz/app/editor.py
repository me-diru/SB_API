from flask_restful import Resource, reqparse, abort
from typing import Dict


class RateEditor(Resource):
    def __init__(self, **kwargs):
        self.backend = kwargs["backend"]
        self.token = kwargs["token"]

        self.parser = reqparse.RequestParser()
        self.parser.add_argument("token", type=str, required=True)

    def put(self, editor_id: int) -> Dict[str, str]:
        args = self.parser.parse_args()

        if args.token != self.token:
            abort(403)
        if self.backend.rate_editor(editor_id):
            return {"status": "ok"}
        else:
            return {"status": "could not find editor"}


class TrainEditor(Resource):
    def __init__(self, **kwargs):
        self.backend = kwargs["backend"]
        self.token = kwargs["token"]

        self.parser = reqparse.RequestParser()
        self.parser.add_argument("token", type=str, required=True)
        self.parser.add_argument("is_spammer", type=bool, required=True)

    def put(self, editor_id: int) -> Dict[str, str]:
        args = self.parser.parse_args()

        if args.token != self.token:
            abort(403)

        if self.backend.train_editor(editor_id, args.is_spammer):
            return {"status": "ok"}
        else:
            return {"status": "could not find editor"}
