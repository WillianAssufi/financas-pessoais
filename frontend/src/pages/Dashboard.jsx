import { useEffect, useState } from "react"
import FormTransacao from "../components/FormTransacao"

function Dashboard({ token }) {
  const [transacoes, setTransacoes] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function buscarTransacoes() {
      const response = await fetch('http://localhost:8000/transacoes/', {
        headers: { 'Authorization': `Bearer ${token}` }
      })
      const dados = await response.json()
      setTransacoes(dados)
      setLoading(false)
    }
    buscarTransacoes()
  }, [])

  function adicionarTransacao(descricao, valor) {
    setTransacoes([...transacoes, { descricao, valor }])
  }

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Logado com sucesso!</p>
      <div>{transacoes.map((t, indice) => (<p key={indice}> {t.descricao} - R$ {t.valor} </p>))}</div>
      <FormTransacao onAdicionar={adicionarTransacao} token={token} />
    </div>
  )
}

export default Dashboard