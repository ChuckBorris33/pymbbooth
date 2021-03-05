import { state } from "./store";

export function setState(newState) {
  state.set(newState);
}

export async function printPhoto(filename) {
  await new Promise((r) => setTimeout(r, 1000)); // User feedback timeout
  const job_id = await window.pywebview.api.print_photo(filename);
  await new Promise((r) => setTimeout(r, 2000));
  const state = await window.pywebview.api.job_state(job_id);
  return state;
}

export async function getLastPhoto() {
  return await window.pywebview.api.get_last_photo();
}

export async function getThumbnailList() {
  return await window.pywebview.api.get_thumbnails();
}

export async function startCapture() {
  return await window.pywebview.api.start_capture();
}

export async function getConfig() {
  return await window.pywebview.api.get_config();
}
