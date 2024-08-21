const footer = document.querySelector('footer')

document.addEventListener('DOMContentLoaded', (e) => {
    const rodapeDireitos = document.createElement('div')
    rodapeDireitos.classList.add('rodape-direitos')

    const textoLayout = `
        <h3 id='direitosCriador'>
        </h3>
    `

    rodapeDireitos.innerHTML = textoLayout
    footer.appendChild(rodapeDireitos)
})