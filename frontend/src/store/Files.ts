import { defineStore } from 'pinia';
import { computed, ref } from 'vue';
import { api } from '@/api'

interface Pipeline {

}

export const useFileStore = defineStore('fileStore', () => {

  const files = ref(<Pipeline[]>[]);
  const isEmptyFileList = computed(() => files.value.length === 0);

  return {
    files,
    isEmptyFileList,

    addFile(file: File) {
      api.sendFiles([file])
      files.value.push({
        name: file.name
      })
    }

  };
});