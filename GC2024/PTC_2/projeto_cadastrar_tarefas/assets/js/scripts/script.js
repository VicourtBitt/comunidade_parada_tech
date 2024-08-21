document.addEventListener("DOMContentLoaded", (e) => {
    const footerRights = document.getElementById('direitosCriador')
    const inputName = document.getElementById('gatherName')
    const inputChore = document.getElementById('gatherChore')
    const selectPrior = document.getElementById('gatherPriority')

    const verificaDireitos = (elem) => {
        const valor = elem.value
        // const verCriador

        if (!valor) {
            elem.innerText = 'Responda o formulário para ver'
        }
    }

    const criarTarefa = (list) => {
        let temInfo = null
        list.forEach((elem) => {
            if (!elem.value) {
                temInfo = false
            }
        })

        if (!temInfo) {
            
        }
    }
    
    const verificarValores = (elem) => {

    }

    verificaDireitos(footerRights)
})

const pegarEspecifico = document.querySelector('#id .classe')
const pegaId = document.getElementById('id')
const pegaClasse = document.getElementsByClassName('classes')
const pegaElementos = document.getElementsByTagName('elemento')



