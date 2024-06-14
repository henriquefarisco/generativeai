document.getElementById('question-form').addEventListener('submit', function(event) {
  event.preventDefault();
  
  const question = document.getElementById('question').value;
  const loadingElement = document.getElementById('loading');
  const responseElement = document.getElementById('response');
  
  loadingElement.style.display = 'block';
  responseElement.style.display = 'none';
  
  fetch('/ask', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ question: question })
  })
  .then(response => response.json())
  .then(data => {
      loadingElement.style.display = 'none';
      responseElement.innerHTML = data.response;
      responseElement.style.display = 'block';
  })
  .catch(error => {
      console.error('Error:', error);
      loadingElement.style.display = 'none';
      responseElement.innerText = 'Ocorreu um erro. Por favor, tente novamente.';
      responseElement.style.display = 'block';
  });
});
