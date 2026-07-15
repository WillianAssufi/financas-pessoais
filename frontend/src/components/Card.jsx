function Card({ titulo, valor, tipo }) {
  return (
    <div style={{
      background: 'white',
      padding: '20px',
      borderRadius: '8px',
      margin: '10px',
      boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
    }}>
      <p style={{ color: 'gray', fontSize: '14px' }}>{titulo}</p>
      <p style={{
        fontSize: '24px',
        fontWeight: 'bold',
        color: tipo === 'receita' ? 'green' : 'red'
      }}>
        R$ {valor}
      </p>
    </div>
  )
}

export default Card