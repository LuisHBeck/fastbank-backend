from core.models import Account

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


def filtering_by_account(model, account, user):
    """
    Filtering the queryset by a specific account

    Args:
        model (class): Models class to filter

    Returns:
        queryset: filtered by the account
    """
    queryset = model.objects.all()
    if account:
        account_obj = Account.objects.get(number=account)
        print(account_obj)
        if (user.is_authenticated and user.is_superuser) or user in account_obj.user.all():
            queryset = queryset.filter(id_account=account)
            return queryset
    return []