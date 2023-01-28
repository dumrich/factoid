def test_homepage_loads(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Factoid')
def test_search_results(self):
    response = self.client.get('/search/?q=moon')
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'The moon is a natural satellite of Earth')

def test_add_fact(self):
    fact = Fact.objects.create(fact='The Earth has one natural satellite, the moon.')
    response = self.client.get('/')
    self.assertContains(response, fact.fact)

def test_delete_fact(self):
    fact = Fact.objects.create(fact='The Earth has one natural satellite, the moon.')
    response = self.client.get('/delete/' + str(fact.id))
    self.assertEqual(response.status_code, 200)

    response = self.client.get('/')
    self.assertNotContains(response, fact.fact)
def test_register_and_login(self):
    response = self.client.get('/register/')
    self.assertEqual(response.status_code, 200)

    data = {'username': 'testuser', 'password': 'testpassword'}
    response = self.client.post('/register/', data)
    self.assertRedirects(response, '/login/')

    response = self.client.post('/login/', data)
    self.assertRedirects(response, '/')

def test_logout(self):
    self.client.login(username='testuser', password='testpassword')
    response = self.client.get('/logout/')
    self.assertRedirects(response, '/')

