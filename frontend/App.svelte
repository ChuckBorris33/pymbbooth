<script>
  import { init, addMessages } from "svelte-i18n";
  import { onMount } from "svelte";
  import { state } from "./store";
  import { AppState } from "./defines";
  import { getConfig } from "./actions";

  import Capture from "./views/Capture.svelte";
  import Intro from "./views/Intro.svelte";
  import Preview from "./views/Preview.svelte";
  import Gallery from "./views/Gallery.svelte";

  import en from "./locale/en.yaml";

  let apiReady = false;

  let stateComponents = {
    [AppState.INTRO]: Intro,
    [AppState.CAPTURE]: Capture,
    [AppState.PREVIEW]: Preview,
    [AppState.GALLERY]: Gallery,
  };

  onMount(async () => {
    window.addEventListener("pywebviewready", async () => {
      const { locale } = await getConfig();
      const dictionary = await import(`./locale/${locale}.yaml`);
      addMessages(locale, dictionary);
      init({
        initialLocale: locale,
      });
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
