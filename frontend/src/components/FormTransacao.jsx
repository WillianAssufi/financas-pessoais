import { useState } from 'react'

function FormTransacao({ onAdicionar, token }) {
  const [descricao, setDescricao] = useState('')
  const [valor, setValor] = useState('')
  const [tipo, setTipo] = useState('receita')

  async function handleSubmit() {
    if (!descricao || !valor) return

    const response = await fetch('http://localhost:8000/transacoes/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ 
        descricao, 
        valor: parseFloat(valor), 
        tipo, 
        data: new Date().toISOString().split('T')[0], 
        categoria_id: 1 
      })
    })
    onAdicionar(descricao, valor)
    setDescricao('')
    setValor('')
  }

  return (
    <div style={{ marginTop: '20px' }}>
      <input
        type="text"
        value={descricao}
        onChange={(e) => setDescricao(e.target.value)}
        placeholder="Descrição"
      />
      <input
        type="number"
        value={valor}
        onChange={(e) => setValor(e.target.value)}
        placeholder="Valor"
      />
      <select value={tipo} onChange={(e) => setTipo(e.target.value)}>
        <option value="receita">Receita</option>
        <option value="despesa">Despesa</option>
      </select>
      <button onClick={handleSubmit}>Adicionar</button>
    </div>
  )
}

export default FormTransacao