from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import MyResource as ResourceModel, db

class ResourceList(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        resources = ResourceModel.query.filter_by(user_id=user_id).all()

        # Convert each resource to a dictionary
        resources_list = [{'id': r.id, 'name': r.name, 'description': r.description} for r in resources]

        return jsonify(resources_list)  # Use jsonify to serialize it properly
    
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()

        # Error handling for missing fields
        if not data or 'name' not in data or 'description' not in data:
            return {'message': 'Missing name or description'}, 400

        new_resource = ResourceModel(name=data['name'], description=data['description'], user_id=user_id)
        db.session.add(new_resource)
        db.session.commit()

        return {'message': 'Resource created'}, 201

class ResourceDetail(Resource):
    @jwt_required()
    def get(self, resource_id):
        resource = ResourceModel.query.get_or_404(resource_id)

        # Convert the resource to a dictionary
        resource_dict = {'id': resource.id, 'name': resource.name, 'description': resource.description}

        return jsonify(resource_dict)  # Use jsonify for serialization
    
    @jwt_required()
    def put(self, resource_id):
        data = request.get_json()

        # Error handling for missing fields
        if not data or 'name' not in data or 'description' not in data:
            return {'message': 'Missing name or description'}, 400

        resource = ResourceModel.query.get_or_404(resource_id)
        resource.name = data['name']
        resource.description = data['description']
        db.session.commit()

        return {'message': 'Resource updated'}
    
    @jwt_required()
    def delete(self, resource_id):
        resource = ResourceModel.query.get_or_404(resource_id)
        db.session.delete(resource)
        db.session.commit()

        return {'message': 'Resource deleted'}
