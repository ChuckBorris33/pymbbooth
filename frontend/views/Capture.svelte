<script>
  import { onMount } from "svelte";

  import { AppState } from "../defines";
  import { startCapture, setState } from "../actions";

  import Spinner from "../components/Spinner.svelte";

  onMount(async () => {
    await startCapture();
    setState(AppState.PREVIEW);
  });
</script>

<style>
  .loading {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .sizer {
    font-size: 8vh;
  }
</style>

<div class="loading">
  <div class="sizer">
    <Spinner />
  </div>
</div>
