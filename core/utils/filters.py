def filtering_by_user(model, user):
    """
    Filtering the queryset by authenticated user

    Args:
        model (class): Models class to filter
        user (object): User to use for filtering

    Returns:
        queryset: filtered by the user.pk 
    """
    queryset = model.objects.all()
        
    if user.is_authenticated and not user.is_superuser:
        return queryset.filter(user=user.pk)
    return queryset