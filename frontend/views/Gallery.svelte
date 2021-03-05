<script>
  import { onMount } from "svelte";
  import { _ } from "svelte-i18n";

  import { AppState } from "../defines";
  import { getThumbnailList, setState } from "../actions";

  import BottomMenu from "../components/BottomMenu.svelte";
  import MenuButton from "../components/MenuButton.svelte";
  import PrintButton from "../components/PrintButton.svelte";

  let photoList = [];
  let selectedPhotoId = null;

  $: padding = photoList.length % 3;
  $: firstPhotoActive = selectedPhotoId === 0;
  $: lastPhotoActive = selectedPhotoId === photoList.length - 1;
  $: detailOpened = selectedPhotoId !== null;

  function selectPhoto(photoID) {
    selectedPhotoId = photoID;
  }

  function prevPhoto() {
    selectedPhotoId = selectedPhotoId - 1;
  }
  function nextPhoto() {
    selectedPhotoId = selectedPhotoId + 1;
  }

  function back() {
    if (detailOpened) {
      selectedPhotoId = null;
    } else {
      setState(AppState.INTRO);
    }
  }

  onMount(async () => {
    photoList = await getThumbnailList();
  });
</script>

<style>
  .gallery {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: stretch;
  }

  .gallery-photos {
    height: 75vh;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    overflow-y: scroll;
    padding-left: 3%;
    padding-right: 3%;
  }

  .gallery-photo {
    width: 30%;
    margin-bottom: 20px;
  }

  .gallery-photo img {
    width: 100%;
    height: auto;
  }

  .gallery-detail {
    width: 100%;
    height: 80vh;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
  }

  .detail-photo {
    display: flex;
    flex-direction: row;
    justify-content: center;
    width: 80%;
    height: 75vh;
  }

  .detail-photo img {
    padding-left: 5vh;
    padding-right: 5vh;
    padding-bottom: 5vh;
    object-fit: scale-down;
    z-index: 1;
  }

  .spacer {
    height: 5vh;
  }

  .nav {
    width: 10%;
    z-index: 2;
  }

  .nav img {
    height: 20vh;
    width: auto;
  }
</style>

<div class="gallery">
  <div class="spacer" />
  {#if !detailOpened}
    <div class="gallery-photos">
      {#each photoList as galeryItem, id}
        <div class="gallery-photo">
          <!-- svelte-ignore a11y-missing-attribute -->
          <img
            src={`./photos/thumbnails/${galeryItem}`}
            on:click={() => selectPhoto(id)} />
        </div>
      {/each}
      {#each { length: padding } as _}
        <div class="gallery-photo" />
      {/each}
    </div>
  {:else}
    <div class="gallery-detail">
      <div class="nav prev">
        <!-- svelte-ignore a11y-missing-attribute -->
        <img
          src="./images/prev.svg"
          class:hidden={firstPhotoActive}
          on:click={prevPhoto} />
      </div>
      <!-- svelte-ignore a11y-missing-attribute -->
      <div class="detail-photo">
        <img src={`./photos/${photoList[selectedPhotoId]}`} />
      </div>
      <div class="nav next">
        <!-- svelte-ignore a11y-missing-attribute -->
        <img
          src="./images/next.svg"
          class:hidden={lastPhotoActive}
          on:click={nextPhoto} />
      </div>
    </div>
  {/if}
  <div class="menu">
    <BottomMenu>
      <MenuButton text={$_('back')} iconName="back" on:click={back} />
      {#if detailOpened}
        <PrintButton filename={photoList[selectedPhotoId]} />
      {/if}
    </BottomMenu>
  </div>
</div>
