def test_with_kwargs(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))

test_with_kwargs(name='shanker', age = 24, location='Hyderabad', cellno=989987)
