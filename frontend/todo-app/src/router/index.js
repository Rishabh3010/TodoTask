import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const guard = (to, from, next) => {
  if(localStorage.getItem('token')) {
    next()
  }
  else {
    next('/login')
  }
};

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      beforeEnter: guard
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
  ]
})

export default router
