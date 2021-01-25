<script>
  import { onMount } from "svelte";
  import { state } from "./store";
  import { AppState } from "./defines";

  import Capture from "./views/Capture.svelte";
  import Intro from "./views/Intro.svelte";
  import Preview from "./views/Preview.svelte";
  import Gallery from "./views/Gallery.svelte";

  let apiReady = false;

  let stateComponents = {
    [AppState.INTRO]: Intro,
    [AppState.CAPTURE]: Capture,
    [AppState.PREVIEW]: Preview,
    [AppState.GALLERY]: Gallery,
  };

  onMount(() => {
    window.addEventListener("pywebviewready", () => {
      apiReady = true;
    });
  });
</script>

<main>
  {#if apiReady}
    <div class="container">
      <svelte:component this={stateComponents[$state]} />
    </div>
  {/if}
</main>
