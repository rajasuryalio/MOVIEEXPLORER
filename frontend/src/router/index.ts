import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ActorsDetail from '@/components/ActorsDetail.vue'
import MoviesDetail from '@/components/MoviesDetail.vue'
import GenresDetail from '@/components/GenresDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/actors',
      name: 'actors',
      component: ActorsDetail,
    },
    {
      path: '/movies',
      name: 'movies',
      component: MoviesDetail,
    },
    {
      path: '/genres',
      name: 'genres',
      component: GenresDetail,
    },
  ],
})

export default router
