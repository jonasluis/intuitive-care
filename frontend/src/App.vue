<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="8">
            <h1 class="text-h4 mb-6">Pesquisa de Operadoras de Saúde</h1>
            <v-text-field
              v-model="termoBusca"
              label="Buscar operadoras"
              append-icon="mdi-magnify"
              clearable
            ></v-text-field>

            <v-skeleton-loader
              v-if="carregando"
              type="table"
              class="mt-4"
            ></v-skeleton-loader>

            <v-data-table
              v-if="operadoras.length > 0 && !carregando"
              :headers="cabecalhos"
              :items="operadoras"
              class="elevation-1"
            >
              <template v-slot:no-data>
                <v-alert type="info" class="ma-2">Nenhum resultado encontrado</v-alert>
              </template>
            </v-data-table>

            <v-alert
              v-if="erro"
              type="error"
              class="mt-4"
            >
              {{ erro }}
            </v-alert>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, watch } from 'vue'
import { buscarOperadoras } from './services/operadoraService'

const termoBusca = ref('')
const operadoras = ref([])
const carregando = ref(false)
const erro = ref(null)

const cabecalhos = [
  { title: 'Registro ANS', key: 'registro_ans' },
  { title: 'CNPJ', key: 'cnpj' },
  { title: 'Razão Social', key: 'razao_social' },
  { title: 'Nome Fantasia', key: 'nome_fantasia' },
  { title: 'Modalidade', key: 'modalidade' },
  { title: 'UF', key: 'uf' },
]

watch(termoBusca, async (novoValor) => {
  if (!novoValor.trim()) {
    operadoras.value = []
    return
  }

  carregando.value = true
  erro.value = null

  try {
    operadoras.value = await buscarOperadoras(novoValor)
  } catch (err) {
    erro.value = err.message
    operadoras.value = []
  } finally {
    carregando.value = false
  }
}, { immediate: false, debounce: 500 }) // Aguarda 500ms antes de buscar
</script>