<script setup lang="ts">
import { onMounted } from 'vue'
import usePlatosStore from '@/stores/platos'
import usePostresStore from '@/stores/postres'
import useBebidasStore from '@/stores/bebidas'
import { storeToRefs } from 'pinia'

const platosStore = usePlatosStore()
const postresStore = usePostresStore()
const bebidasStore = useBebidasStore()

const { platos } = storeToRefs(platosStore)
const { postres } = storeToRefs(postresStore)
const { bebidas } = storeToRefs(bebidasStore)

onMounted(async () => {
  await platosStore.getAll()
  await postresStore.getAll()
  await bebidasStore.getAll()
})
</script>

<template>
  <div class="menu-digital">
    <div class="menu-header">
      <h1>Menú Digital</h1>
      <h5 class="subtitle">Restaurant "La Cosa Nostra"</h5>
    </div>
    <section class="menu-section">
      <h2 class="section-title">Platos</h2>
      <div class="items-list">
        <div v-for="plato in platos" :key="plato.id" class="menu-item">
          <div class="item-content">
            <span class="name">{{ plato.nombre }}</span>
            <span class="separator">-</span>
            <span class="description">{{ plato.descripcion }}</span>
          </div>
          <span class="price">${{ plato.precio }}</span>
        </div>
      </div>
    </section>
    <section class="menu-section">
      <h2 class="section-title">Postres</h2>
      <div class="items-list">
        <div v-for="postre in postres" :key="postre.id" class="menu-item">
          <div class="item-content">
            <span class="name">{{ postre.nombre }}</span>
            <span class="separator">-</span>
            <span class="description">{{ postre.descripcion }}</span>
          </div>
          <span class="price">${{ postre.precio }}</span>
        </div>
      </div>
    </section>
    <section class="menu-section">
      <h2 class="section-title">Bebidas</h2>
      <div class="items-list">
        <div v-for="bebida in bebidas" :key="bebida.id" class="menu-item">
          <div class="item-content">
            <span class="name">{{ bebida.nombre }}</span>
            <span class="separator">-</span>
            <span class="category-inline">{{ bebida.categoria_nombre }}</span>
          </div>
          <span class="price">${{ bebida.precio }}</span>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>

.menu-digital {
  max-width: 1060px;
  margin: 0 auto;
  padding: 1px 20px;
  background: #ffffff;
  min-height: 100vh;
  background-image: url('@/assets/fondo.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  min-height: 100vh;
}

.menu-header {
  text-align: center;
  margin-bottom: 1px;
  padding: 40px 0;
}

.menu-header h1 {
  font-size: 48px;
  color: #2c3e50;
  margin-bottom: 10px;
  font-family: 'Georgia', serif;
}

.subtitle {
  font-size: 20px;
  color: #7f8c8d;
  font-style: italic;
}

.menu-section {
  margin-bottom: 40px;
}

.section-title {
  font-size: 32px;
  color: #2c3e50;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 2px solid #ecf0f1;
  font-family: 'Georgia', serif;
}

.items-list {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.menu-item {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 8px 0;
  border-bottom: 1px dotted #ddd;
  gap: 20px;
  transition: all 0.1s ease;  /*de aca para abajo para la modificacion de la seleccion del item */
  border-left: 3px solid transparent;  
  padding: 8px 0 8px 10px;  
}

.menu-item:last-child {
  border-bottom: none;
}

.menu-item:hover {
  border-left: 3px solid #415c77;  
  padding-left: 15px;  /* ← Se mueve un poco a la derecha */
  border-bottom: 2px solid #415c77;
}

.menu-item:hover .name {
  color: #415c77;  /* ← Nombre cambia de color */
  font-weight: 700;  /* ← Se pone más negrita */
}

.item-content {
  display: flex;
  align-items: baseline;
  gap: 8px;
  flex: 1;
  min-width: 0;
}

.name {
  font-weight: 600;
  color: #2c3e50;
  font-size: 16px;
  white-space: nowrap;
}

.separator {
  color: #95a5a6;
  font-weight: 300;
}

.description,
.category-inline {
  color: #7f8c8d;
  font-size: 14px;
  font-style: italic;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.price {
  font-size: 16px;
  font-weight: bold;
  color: #42b983;
  white-space: nowrap;
  margin-left: auto;
}

/* Responsive */
@media (max-width: 768px) {
  .menu-header h1 {
    font-size: 36px;
  }
  
  .section-title {
    font-size: 28px;
  }
  
  .item-content {
    flex-direction: column;
    gap: 4px;
  }
  
  .separator {
    display: none;
  }
}
</style>