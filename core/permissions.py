from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
    

class DeletePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True
    

class NormalUserGet(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        if request.method == 'GET':
            if request.user.is_authenticated:
                return True
            return False 
        return False
    

class NormalUserPost(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        if request.method == 'POST': 
            if request.user.is_authenticated:
                return True
            return False
        return False
    
    
class NormalUserGetPost(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        if request.method in 'GET POST': 
            if request.user.is_authenticated:
                return True
            return False
        return False
       

class NormalUserGetPostPut(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        if request.method in 'GET POST PUT':
            if request.user.is_authenticated:
                return True
            return False
        return False
    

class NormalUserGetPostPatch(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        if request.method in 'GET POST PATCH':
            if request.user.is_authenticated:
                return True
            return False
        return False
    

class NormalUserPostPut(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        if request.method in 'POST PUT':
            if request.user.is_authenticated:
                return True
            return False
        return False