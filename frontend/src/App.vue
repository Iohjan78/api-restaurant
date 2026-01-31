<script setup>
import { RouterLink, RouterView, useRoute } from 'vue-router'
import { computed } from 'vue'
import { Icon } from '@iconify/vue'

const route = useRoute()


const isAdminRoute = computed(() => {
  return route.path.startsWith('/admin') || 
         route.path.startsWith('/platos') || 
         route.path.startsWith('/postres') || 
         route.path.startsWith('/bebidas') || 
         route.path.startsWith('/categorias')
})
</script>

<template>
  <div class="app-container">
    <header v-if="!isAdminRoute" class="public-header">
      <div class="header-content">
        <router-link to="/admin" class="btn-admin">
          Administrar
        </router-link>
      </div>
    </header>


    <header v-else class="admin-header">
      <div class="header-content">
        <h2>Back Office</h2>
        <nav class="admin-nav">
          <RouterLink to="/">
            <Icon icon="fa:chevron-circle-left" width="15" height="15" />
             Volver al Menú
            </RouterLink>
          <RouterLink to="/categorias">Categorías</RouterLink>
          <RouterLink to="/platos">Platos</RouterLink>
          <RouterLink to="/postres">Postres</RouterLink>
          <RouterLink to="/bebidas">Bebidas</RouterLink>
        </nav>
      </div>
    </header>

    <RouterView />
  </div>
  <footer class="app-footer">
      <div class="footer-content">
        <p>2025 La Cosa Nostra - Ristorante Italiana</p>
        <p class="footer-info">Universidad Nacional del Comahue, Viedma, Río Negro</p>
        <p class="footer-info">Tecnicatura de Desarrollo Web</p>
        <p class="footer-dev">Desarrollado por Juan Manuel Yurcombich - TP Final con Vue · Flask · Postgres · Docker</p>
      </div>
    </footer>
</template>

<style scoped>
.app-container {
  min-height: 100vh;
}


.public-header {
  background-image: 
    url('@/assets/letras1.png'),  
    url('@/assets/fondo-textura.jpg');  
  background-size: 
    auto 110%,  
    cover;  
  background-position: 
    center,  
    center;  
  background-repeat: 
    no-repeat,  
    no-repeat; 
  width: 100%;
  height: 120px;
  position: relative;
}

.public-header .header-content {
  max-width: 1060px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
}


.btn-admin {
  background: white;
  color: #2c3e50;
  padding: 10px 20px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  position: absolute;  /* ← Posición absoluta */
  top: 20px;
  right: 20px;
}

.btn-admin:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255,255,255,0.3);
}

/* Header de administración */
.admin-header {
  background: #d7b67e;
  color: #2c3e50;
  padding: 15px 0;
  box-shadow: 0 2px 4px rgba(44,62,80, 0.1);
}

.admin-header .header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.admin-header h2 {
  font-size: 24px;
  margin: 0 0 15px 0;
}

.admin-nav {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

.admin-nav a {
  color: #2c3e50;
  text-decoration: none;
  padding: 8px 16px;
  border-radius: 6px;
  transition: background-color 0.2s ease;
}

.admin-nav a:hover {
  background-color: #ac9265;
}

.admin-nav a.router-link-active {
  background-color: #ac9265;
  font-weight: bold;
}

/* Responsive */
@media (max-width: 768px) {
  .public-header .header-content {
    flex-direction: column;
    gap: 15px;
    text-align: center;
  }
  
  .admin-nav {
    flex-direction: column;
    gap: 10px;
  }
}
</style>