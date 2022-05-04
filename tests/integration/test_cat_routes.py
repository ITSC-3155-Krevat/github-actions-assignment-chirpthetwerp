def test_get_all_cats(test_app):
    res = test_app.get('/cats')

    assert res.status_code == 200
    assert b'No CATS! GO make a Cat.' in res.data

def test_create_cat(test_app):
    res = test_app.post('/cats', data={
        'name': 'Piero',
        'breed': 'Orange',
        'numLegs': 4,
    }, follow_redirects=True)

    assert res.status_code == 200
    assert 'Piero' in res.data
    assert 'Orange' in res.data
    assert '4' in res.data