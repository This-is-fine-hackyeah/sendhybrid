<template>
  <q-dialog
    ref="dialogRef"
    @hide="onDialogHide"
  >
    <q-card :style="{'width': '700px'}">
      <div class="icon-wrapper text-center">
        {{ errors }}
      </div>
    </q-card>
  </q-dialog>
</template>

<script lang="ts">
import { useDialogPluginComponent } from 'quasar'
</script>

<script setup lang="ts">
const { dialogRef, onDialogHide } = useDialogPluginComponent()
defineEmits([...useDialogPluginComponent.emits])
defineProps({
  errors: {
    type: Object,
    required: true
  }
})
</script>
