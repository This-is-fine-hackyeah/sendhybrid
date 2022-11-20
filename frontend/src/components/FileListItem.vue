<template>
<div class="row file-wrapper">
  <div class="col-5 column justify-center">
    {{ file.name }}
  </div>
  <div class="col-3 text-center column justify-center">
    <div v-if="fileStatus !== null">
      <q-icon :name="fileStatus === true ? outlinedDone : outlinedDangerous" size="20px"/>
    </div>
  </div>
  <div class="col-1 text-center column justify-center">
    <q-btn label="Sprawdź" class="button-check" @click="checkDetails"/>
  </div>
  <div class="col-1 text-center"></div>
  <div class="col-1 text-center column justify-center">
    <q-btn label="Metadane" class="button-metabase" />
  </div>
</div>
</template>

<script setup lang="ts">
import { api } from '@/api'
import { ref } from 'vue'
import { outlinedDone, outlinedDangerous } from '@quasar/extras/material-icons-outlined'
import FailureDetails from './FailureDetails.vue'
import { useQuasar } from 'quasar'

const fileStatus = ref(null)
const props = defineProps({
  file: {
    type: Object,
    required: true
  }
})

const $q = useQuasar()

let errors = {}
const checkDetails = () => {
  $q.dialog({
    component: FailureDetails,
    componentProps: {
      errors
    }
  })
}

const checkStatus = async () => {
  const report = await api.checkStatusForDocument(props.file.id)
  if (report.format === null) {
    setTimeout(checkStatus, 2000)
  } else {
    fileStatus.value = report.report
    errors = report
  }
}

checkStatus()
</script>

<style lang="sass" scoped>
.file-wrapper
  border: 0.5px solid gray
  border-top: none
  min-height: 63px
  padding: 8px
  margin-right: 20px

.button-check, .button-metabase
  width: 100%
  text-transform: none
  border-radius: 4px

.button-check
  background: #2C347D
  color: white

.button-metabase
  background: #D5D5D5
  color: #3D4043
</style>
