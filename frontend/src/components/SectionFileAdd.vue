<template>
  <div
    class="row flex-center"
    :class="{'full-height': !compactMode, 'pt-10': compactMode}"
  >
    <div class="select-files-wrapper">
      <div :class="{ 'text-wrapper': true, p5: !compactMode, p2: compactMode }">
        <div class="row items-center text-gray">
          <div class="q-px-xs">
            <q-icon
              :name="outlinedAttachFile"
              size="20px"
            />
          </div>
          <h2 :class="compactMode ? 'text-lg' : 'text-base'">
            Przeciągnij pliki tutaj
          </h2>
        </div>

        <div
          v-if="!compactMode"
          class="p2"
        >
          <p class="text-md text-gray text-center">
            lub
          </p>
        </div>
        <div :class="{'q-pt-sm': compactMode, 'row justify-center': true}">
          <label for="file-upload" class="custom-file-upload">
            <q-icon :name="outlinedAdd" /> Przeglądaj komputer
          </label>
          <input id="file-upload" ref="uploadedFiles" type="file" multiple v-on:change="onFileUpload" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { outlinedAdd, outlinedAttachFile } from '@quasar/extras/material-icons-outlined'
import { ref } from 'vue'
import { useFileStore } from '@/store/Files'

const { addFile } = useFileStore()
const uploadedFiles = ref(null)

const onFileUpload = () => {
  for (const file of uploadedFiles.value.files) {
    addFile(file)
  }
}

defineProps({
  compactMode: {
    type: Boolean,
    default: true
  }
})

</script>

<style lang="sass" scoped>
.select-files-wrapper
  // https://kovart.github.io/dashed-border-generator/
  background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' rx='20' ry='20' stroke='%236D6D6CFF' stroke-width='5' stroke-dasharray='25%2c 17' stroke-dashoffset='0' stroke-linecap='square'/%3e%3c/svg%3e")
  border-radius: 20px
  padding: 0 15vw

.p5
  padding: 70px 0

.p2
  padding: 20px

.button-browse-computer-small
  font-size: 18px
  padding: 16px 30px

input[type="file"]
  display: none

.custom-file-upload
  border: 1px solid #ccc
  display: inline-block
  padding: 6px 12px
  cursor: pointer
  background: #2D63D9
  border-radius: 4px
  color: white
</style>
