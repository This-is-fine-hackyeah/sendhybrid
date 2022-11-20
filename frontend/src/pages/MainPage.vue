<template>
  <div>
    <q-layout view="hHh Lpr lff">
      <q-drawer
        v-model="drawer"
        show-if-above
        :width="200"
        :breakpoint="500"
        bordered
        class="sidebar-wrapper"
      >
        <div class="row justify-center items-center py-10 text-base">
          <div class="pr-3">
            <img src="/images/logo.png" />
          </div>
          <div>
            Send hybrid
          </div>
        </div>
        <q-list>
          <template v-for="(menuItem, index) in menuList" :key="index">
            <q-item
              clickable
              :active="menuItem.id === selectedEntry"
              v-ripple
              @click="selectedEntry = menuItem.id"
              class="h-[56px]"
            >
              <q-item-section avatar>
                <q-icon :name="menuItem.icon" />
              </q-item-section>
              <q-item-section>
                {{ menuItem.label }}
              </q-item-section>
            </q-item>
            <div class="separator" v-if="menuItem.separator"></div>
          </template>

        </q-list>
      </q-drawer>

      <q-page-container>
        <q-page padding style="height:100vh; background: #F8F9FF;">
          <div v-if="selectedEntry === 'convert'" class="h-full">
            <file-list />
          </div>
          <div v-if="selectedEntry === 'reports'">
            TODO
          </div>
        </q-page>
      </q-page-container>
    </q-layout>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import FileList from '@/components/FileList.vue'

const menuList = [
  {
    id: 'convert',
    icon: 'pie_chart',
    label: 'Zweryfikuj pliki',
    separator: false
  },
  {
    id: 'reports',
    icon: 'summarize',
    label: 'Lista raportów',
    separator: false
  },
  {
    id: 'history',
    icon: 'history_edu',
    label: 'Historia',
    separator: false
  },
  {
    id: 'agents',
    icon: 'person',
    label: 'Agents',
    separator: true
  },
  {
    id: 'settings',
    icon: 'settings',
    label: 'Ustawienia',
    separator: false
  },
  {
    id: 'help',
    icon: 'help',
    iconColor: 'primary',
    label: 'Pomoc',
    separator: false
  }
]

const drawer = ref(false)
const selectedEntry = ref(menuList[0].id)

</script>

<style lang="sass" scoped>
:deep(.sidebar-wrapper)
  background: #363740
  color: #A4A6B3

  .q-item--active
    color: #DDE2FF

.separator
  border-top: 0.5px solid #DFE0EB

</style>
