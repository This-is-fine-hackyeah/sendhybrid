import { defineStore } from 'pinia';
import { ref } from 'vue';

export enum UserRole {
  REGULAR = 'regular',
  ADMIN = 'admin'
}

export const useUserStore = defineStore('userState', () => {

  const role = ref(UserRole.REGULAR);

  return {
    setUserRole(roleParam: UserRole) {
      role.value = roleParam;
    }
  };
});