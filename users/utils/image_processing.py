def upload_user_photo(instance, filename):
	"""_summary_

	Args:
		instance (obj): photo instance
		filename (str): original file name

	Returns:
		archive name: return the archive name formatted
	"""
	return f'{instance.pk}-{filename}'