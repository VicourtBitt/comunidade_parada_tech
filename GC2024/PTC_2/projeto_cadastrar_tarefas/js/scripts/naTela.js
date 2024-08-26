export const verificaDireitos = (elem) => {
    const valor = elem.value
    // const verCriador

    if (!valor) {
        elem.innerText = 'Responda o formulário para ver'
    }
}

export const criarTarefa = async (obj, tabela, type) => {
    let info = null

    // Realiza algo dependendo do tipo de ação
    if (type == 'input') {
        info = pegarValores(obj)
    } else if (type == 'json') {
        info = obj
    }

    // Cria um elemento para popular ele depoiis
    const divTarefa = document.createElement('div')
    divTarefa.classList.add('cada-tarefa')

    const tarefaLayout = `
        <h2 class='tarefa-nome'>
            ${info.tarefa}
        </h2>

        <h3 class='tarefa-responsavel'>
            ${info.nome}
        </h3>

        <h4 class='tarefa-prioridade'>
            ${info.prioridade}
        </h4>

        <button class='tarefa-button'>
            X
        </button>
    `

    // Transformar em função prob
    const btnTarefas = document.querySelectorAll('.tarefa-button')
    btnTarefas.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            btn.parentNode
        })
    })

    divTarefa.innerHTML = tarefaLayout
    tabela.appendChild(divTarefa)
}

// Transforma os valores dos nodes em um literal
const pegarValores = (obj) => {
    return {
        nome: obj.name.value,
        tarefa: obj.tarefa.value,
        prioridade: obj.prioridade.value
    }
}

// Vê o JSON
export const verificaJSON = async (tabela) => {
    const tarefas = await fetch('http://localhost:3000/tarefas')
    const info = await tarefas.json()
    info.forEach((tarefa) => {
        criarTarefa(tarefa, tabela, 'json')
    })
}

// Posta uma tarefa
export const postarTarefa = async (obj) => {
    const info = pegarValores(obj)
    const post = await fetch('http://localhost:3000/tarefas', {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify(info)
    })
}

// Medo
export const removerObj = async () => {
    
}