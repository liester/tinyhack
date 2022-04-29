const uiOptions = [
    'vanilla js',
    'react',
    'vue',
    'svelte',
    'angular',
    'jquery',
    'gatsby'

]

const apiOptions = [
    'express',
    'java',
    'python',
    'ruby on rails',
    'django',
    'C#'
]

const persistenceOptions = [
    'mongo',
    'postgres',
    'redis',
    'file system',
    'mysql',
    's3'
]

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  }

const getRandomProject = (projectSize) => {
    return fetch(`https://httpbin.org/anything?project-size=${projectSize}`, {

    });
}

const generateCategories = async () => {
    // const categories = await getRandomProject()
    //     .then(response => response.json());
    // document.getElementById('result').textContent = JSON.stringify(categories);
    // return Promise((resolve, reject) => {
        // setTimeout(()=> {
        // }, 3000)
    // })
    const persistence = getRandomInt(persistenceOptions.length)
    const api = getRandomInt(apiOptions.length)
    const ui = getRandomInt(uiOptions.length)

    document.querySelector('#ui-category .spinner-value').textContent = uiOptions[ui];
    document.querySelector('#api-category .spinner-value').textContent = apiOptions[api];
    document.querySelector('#persistence-category .spinner-value').textContent = persistenceOptions[persistence];
}