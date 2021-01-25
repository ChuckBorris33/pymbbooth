import { writable } from "svelte/store";

import { AppState } from "./defines";

export const state = writable(AppState.INTRO);
