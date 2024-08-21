import { verificaDireitos, criarTarefa , verificaJSON, postarTarefa} from "./naTela.js"

document.addEventListener("DOMContentLoaded", async (e) => {
    const footerRights = document.getElementById('direitosCriador')
    const tabelaInfo = document.getElementById('tabela-info')
    const form = document.getElementById('gather')
    const inputName = document.getElementById('gatherName')
    const inputChore = document.getElementById('gatherChore')
    const selectPrior = document.getElementById('gatherPriority')

    const objElementos = {
        name: inputName, 
        tarefa: inputChore, 
        prioridade: selectPrior
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault()
        await criarTarefa(objElementos, tabelaInfo, 'input')
        await postarTarefa(objElementos)
        form.reset()
    })

    verificaJSON(tabelaInfo)
    verificaDireitos(footerRights)
})




