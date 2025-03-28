import axios from 'axios'

export async function buscarOperadoras(termo) {
  if (!termo.trim()) return []
  
  try {
    const resposta = await axios.get(`/api/operadoras/buscar?q=${encodeURIComponent(termo)}`)
    return resposta.data
  } catch (error) {
    throw new Error('Erro ao buscar operadoras. Por favor, tente novamente.')
  }
}