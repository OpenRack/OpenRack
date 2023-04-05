﻿// Decompiled with JetBrains decompiler
// Type: cYo.Projects.ComicRack.Viewer.Views.IComicBrowser
// Assembly: ComicRack, Version=1.0.5915.38777, Culture=neutral, PublicKeyToken=b3ca110c99b4b731
// MVID: E9032406-66BB-46BB-A802-D697DB44DA19
// Assembly location: C:\Program Files\ComicRack\ComicRack.exe

using cYo.Projects.ComicRack.Engine;
using cYo.Projects.ComicRack.Engine.Database;
using System;
using System.Collections.Generic;

namespace cYo.Projects.ComicRack.Viewer.Views
{
  public interface IComicBrowser : IGetBookList
  {
    string SelectionInfo { get; }

    ComicLibrary Library { get; }

    bool SelectComic(ComicBook comic);

    bool SelectComics(IEnumerable<ComicBook> comics);

    Guid GetBookListId();

    DisplayListConfig ListConfig { get; set; }
  }
}
