<template>
  <div class="h-full column">
    <div class="bg-white w-full py-2 px-4">
        <p class="text-bold text-lg m-0">
          Zweryfikuj swoje dokumenty
        </p>
    </div>
    <div class="pl-5">
      <ol class="pt-8 list-decimal text-xs">
        <li>Wgraj dokumenty, aby sprawdzić ich zgodność z wymaganiami Operatora Wyznaczonego</li>
        <li>Gdy dokument będzie sformatowany poprawnie, dokonamy jego konwersji na PDF</li>
        <li>W przypadku niezgodności dokumentu, sprawdź <strong>Akcje</strong> i wygeneruj raport o błędach.</li>
      </ol>
    </div>
    <div
      class="col column"
      :ondrop="dropHandler"
      @dragenter.prevent
      @dragover.prevent
    >
      <section-file-add :compact-mode="!isEmptyFileList"/>
      <div
        v-if="files.length > 0"
        class="col column flex-center text-dark-gray pt-10"
      >
        <div class="file-list-header">
          <div class="row text-xs text-bold bg-white q-py-sm">
            <div class="col-5 text-left q-pl-sm">
              Nazwa pliku
            </div>
            <div class="col-3 text-center">
              Status zgodności
            </div>
            <div class="col-1 text-center">
              Uwagi
            </div>
            <div class="col-1 text-center">
            </div>
            <div class="col-1 text-center">
              Metadane
            </div>
          </div>
        </div>
        <q-scroll-area
          class="files-section w-full col"
          visible
        >
          <file-list-item
            v-for="(file, iter) in files"
            :key="iter"
            :file="file"
          />
        </q-scroll-area>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import SectionFileAdd from './SectionFileAdd.vue'
import FileListItem from './FileListItem.vue'
import { useFileStore } from '@/store/Files'

import { storeToRefs } from 'pinia'
const { isEmptyFileList, files } = storeToRefs(useFileStore())
const { addFile } = useFileStore()

const dropHandler = async (ev) => {
  ev.preventDefault()

  if (ev.dataTransfer.items) {
    [...ev.dataTransfer.items].forEach((item, i) => {
      if (item.kind === 'file') {
        addFile(item.getAsFile())
      }
    })
  } else {
    [...ev.dataTransfer.files].forEach((file, i) => {
      addFile(file)
    })
  }
}
</script>

<style lang="sass" scoped>
.file-list-header
  width: 100%
  padding-right: 20px
  > div
    border: 0.5px solid gray
    border-top-right-radius: 10px
    border-top-left-radius: 10px
    padding: 8px
</style>
