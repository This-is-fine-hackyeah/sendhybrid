<template>
  <div class="flex justify-center items-center h-screen">
    <div>
      <q-btn color="green" text-color="white" label="Admin" rounded @click="updateUserRole(UserRole.ADMIN)" />
    </div>
    <div>
      <q-btn color="green" text-color="white" label="Regular user" rounded @click="updateUserRole(UserRole.REGULAR)" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { UserRole, useUserStore } from '@/store/User'

const { setUserRole } = useUserStore()
const router = useRouter()

const updateUserRole = (role) => {
  setUserRole(role)
  router.push({ name: 'MainPage' })
}
</script>
